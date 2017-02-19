# -*- coding: utf-8 -*-
"""
rhizopathy - tube.py
Created on 2/19/17.

Class for storing information about Tubes which contain collections of Roots.
"""
# Stdlib
import logging

# Third Party Code
# Custom Code
from rhizopathy.constants.fields import ROOT_FINAL
from rhizopathy.exc import TubeError
from rhizopathy.models.root import Root

log = logging.getLogger(__name__)


class Tube(object):
    def __init__(self, tubenumber):
        self.tubeNumber = tubenumber
        self.roots = []
        self.maxSessionCount = 0
        # self.tipStats = ''  # XXX Commented out until code using it is ported over
        # self.sessionDates = {}  # XXX Commented out until code using it is ported over
        # self.index = 0  # XXX Commented out until code using it is ported over

    def __iter__(self):
        for root in self.roots:
            yield root

    def __len__(self):
        return len(self.roots)

    def _add_root(self, root):
        root.set('Tube#', self.tubeNumber)
        self.roots.append(root)

    def insert_or_update_root(self, root):
        if not isinstance(root, Root):
            raise TubeError('Invalid type provided: {}'.format(type(root)))

        # insert root if the root identity is new
        insert = True
        for existingRoot in self:
            if root.identity == existingRoot.identity:
                insert = False
                # If there was a change, update the root attributes
                if existingRoot.isAlive.startswith('A') and root.isAlive.startswith(('G', 'D')):
                    # root changed from A to G
                    log.debug('Changing root from A to {}'.format(root.isAlive))
                    existingRoot.set('DeathSession', root.get('DeathSession'))
                    existingRoot.isAlive = root.isAlive
                elif existingRoot.isAlive.startswith(('G', 'D')) and root.isAlive.startswith('A'):
                    # root changed from G to A
                    log.debug('Changing root from {} to {}'.format(existingRoot.isAlive, root.isAlive))
                    existingRoot.set('DeathSession', '')
                    existingRoot.isAlive = root.isAlive
        # add the root to the tube
        if insert:
            # possible to insert a root at the last session.  likely rare though.
            # need to finalize this root before adding it into the tube.
            log.debug('Adding root to tube %s' % (str(root.identity)))
            self._add_root(root)
        return True

    def finalize_root(self, root_obj, root_fields):
        finalized = False
        for existingRoot in self:
            if root_obj.identity == existingRoot.identity:
                if root_obj.get('Session#') == self.maxSessionCount:
                    existingRoot.highestOrder = root_obj.get('Order')
                if existingRoot.isAlive.startswith('A'):
                    existingRoot.set('DeathSession', 0)
                    existingRoot.censored = 1
                # XXX Icky!
                if existingRoot.isAlive.startswith(('D', 'G')):
                    existingRoot.censored = 0
                # Update custom fields which are set when the root is finalized
                for attr, state in root_fields.additional_fields.items():
                    if state != ROOT_FINAL:
                        continue
                    existingRoot.set(attr, root_obj.get(attr))
                finalized = True

        return finalized

    # Commented out until synthesis data is implemented.
    # def insert_synthesis_data(self, sdata):
    #     for root_obj in self:
    #         # log.debug('Inserting synthesis data for {}'.format(root_obj.identity))
    #         sd = sdata.get(root_obj.identity, {})
    #         if not sd:
    #             log.warning('Did not get synthesis data for {}'.format(root_obj.identity))
    #             continue
    #         # log.debug(sd)
    #         for k, v in sd.items():
    #             root_obj.set(k, v)
