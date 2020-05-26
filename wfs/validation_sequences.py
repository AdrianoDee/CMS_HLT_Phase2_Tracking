import FWCore.ParameterSet.Config as cms
from  Configuration.StandardSequences.Validation_cff import *
from validation_modules import *
from prevalidation_modules import *

validation_original = cms.Path(hltPhase2TrackValidatorPixelTrackingOnly+hltPhase2TrackValidatorTrackingOnly)

validation_purel1 = cms.Path(hltPhase2TrackValidatorL1)

validation_l1initial = cms.Path(hltPhase2TrackValidatorPixelTrackingOnly + hltPhase2TrackValidatorTrackingOnly + hltPhase2TrackValidatorL1)
